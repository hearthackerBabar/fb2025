#!/usr/bin/env python3
"""
Facebook Login Tool for Termux
A beautiful terminal-based Facebook login validator
"""

import requests
import re
import sys
import os
from getpass import getpass
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.spinner import Spinner
from rich.align import Align
from rich import box
import time

console = Console()

class FacebookLogin:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0'
        })
    
    def get_login_form_data(self):
        """Get the login form data from Facebook's mobile login page"""
        try:
            # First, get the main login page
            url = 'https://mbasic.facebook.com/login.php'
            response = self.session.get(url)
            
            if response.status_code != 200:
                return None
            
            # Extract all necessary form data with more robust patterns
            patterns = {
                'lsd': [r'name="lsd" value="([^"]*)"', r'"LSD",\[],{"token":"([^"]*)"'],
                'jazoest': [r'name="jazoest" value="([^"]*)"'],
                'm_ts': [r'name="m_ts" value="([^"]*)"'],
                'li': [r'name="li" value="([^"]*)"'],
                'try_number': [r'name="try_number" value="([^"]*)"'],
                'unrecognized_tries': [r'name="unrecognized_tries" value="([^"]*)"']
            }
            
            form_data = {}
            
            for field, pattern_list in patterns.items():
                value = ''
                for pattern in pattern_list:
                    match = re.search(pattern, response.text)
                    if match:
                        value = match.group(1)
                        break
                form_data[field] = value
            
            # Set default values if not found
            form_data.setdefault('try_number', '0')
            form_data.setdefault('unrecognized_tries', '0')
            
            return form_data
            
        except Exception as e:
            return None
    
    def login(self, email, password):
        """Attempt to login to Facebook using multiple methods"""
        try:
            # Method 1: Try with free-fb approach (most reliable)
            success, result = self._try_free_fb_method(email, password)
            if success:
                return success, result
            
            # Method 2: Try basic mbasic login
            success, result = self._try_mbasic_login(email, password)
            if success:
                return success, result
            
            # Method 3: Try touch.facebook.com
            success, result = self._try_touch_login(email, password)
            return success, result
                
        except requests.exceptions.Timeout:
            return False, "Request timeout - check your internet connection"
        except requests.exceptions.ConnectionError:
            return False, "Connection error - check your internet connection"
        except requests.exceptions.RequestException as e:
            return False, f"Network error: {str(e)}"
        except Exception as e:
            return False, f"Unexpected error: {str(e)}"
    
    def _try_free_fb_method(self, email, password):
        """Try the free-fb.com method (most reliable)"""
        try:
            # This uses a different approach that's more reliable
            url = 'https://free.facebook.com/login.php'
            
            # Get the login page first
            response = self.session.get(url)
            if response.status_code != 200:
                return False, "Cannot access Facebook free version"
            
            # Extract form data
            form_data = {}
            lsd_match = re.search(r'name="lsd" value="([^"]*)"', response.text)
            jazoest_match = re.search(r'name="jazoest" value="([^"]*)"', response.text)
            
            if lsd_match:
                form_data['lsd'] = lsd_match.group(1)
            if jazoest_match:
                form_data['jazoest'] = jazoest_match.group(1)
            
            # Prepare login payload
            payload = {
                'email': email,
                'pass': password,
                'login': 'Log In',
                **form_data
            }
            
            # Submit login
            self.session.headers.update({
                'Referer': url,
                'Origin': 'https://free.facebook.com',
                'Content-Type': 'application/x-www-form-urlencoded'
            })
            
            response = self.session.post(url, data=payload, allow_redirects=True, timeout=30)
            
            # Check success
            if ('home.php' in response.url or 
                'welcome' in response.text.lower() or
                'timeline' in response.text.lower()):
                
                username = self._extract_username_simple(response)
                return True, username
            
            # Check for errors
            if 'checkpoint' in response.url:
                return False, "Account requires verification (2FA enabled)"
            elif 'login.php' in response.url or 'login_attempt' in response.url:
                return False, "Incorrect username or password"
            
            return False, "Login failed with free.facebook.com method"
            
        except Exception as e:
            return False, f"Free FB method failed: {str(e)}"
    
    def _try_mbasic_login(self, email, password):
        """Try mbasic.facebook.com login"""
        try:
            url = 'https://mbasic.facebook.com/login.php'
            response = self.session.get(url)
            
            if response.status_code != 200:
                return False, "Cannot access mbasic Facebook"
            
            # Get form data
            form_data = self.get_login_form_data()
            if not form_data:
                return False, "Cannot get form data from mbasic"
            
            # Login payload
            payload = {
                'email': email,
                'pass': password,
                'login': 'Log In',
                **form_data
            }
            
            # Submit
            response = self.session.post(
                'https://mbasic.facebook.com/login/device-based/regular/login/',
                data=payload,
                allow_redirects=True,
                timeout=30
            )
            
            # Check success
            if 'home.php' in response.url:
                username = self._extract_username_simple(response)
                return True, username
            elif 'checkpoint' in response.url:
                return False, "Account requires verification"
            elif 'login.php' in response.url:
                return False, "Incorrect username or password"
            
            return False, "mbasic login method failed"
            
        except Exception as e:
            return False, f"mbasic method failed: {str(e)}"
    
    def _try_touch_login(self, email, password):
        """Try touch.facebook.com login"""
        try:
            url = 'https://touch.facebook.com/login.php'
            
            # Update user agent for touch version
            self.session.headers.update({
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1'
            })
            
            response = self.session.get(url)
            if response.status_code != 200:
                return False, "Cannot access touch Facebook"
            
            # Extract form data
            lsd_match = re.search(r'name="lsd" value="([^"]*)"', response.text)
            form_data = {'lsd': lsd_match.group(1)} if lsd_match else {}
            
            # Login payload
            payload = {
                'email': email,
                'pass': password,
                'login': 'Log In',
                **form_data
            }
            
            # Submit
            response = self.session.post(url, data=payload, allow_redirects=True, timeout=30)
            
            # Check success
            if ('home.php' in response.url or 
                'timeline' in response.text.lower()):
                username = self._extract_username_simple(response)
                return True, username
            elif 'checkpoint' in response.url:
                return False, "Account requires verification"
            elif 'login.php' in response.url:
                return False, "Incorrect username or password"
            
            return False, "Touch login method failed"
            
        except Exception as e:
            return False, f"Touch method failed: {str(e)}"
    
    def _extract_username_simple(self, response):
        """Simple username extraction"""
        try:
            # Try title extraction
            title_match = re.search(r'<title>([^<]+)</title>', response.text, re.IGNORECASE)
            if title_match:
                title = title_match.group(1)
                # Clean up the title
                username = re.sub(r'\s*[\|\-]\s*Facebook.*$', '', title).strip()
                if username and len(username) > 1 and 'facebook' not in username.lower():
                    return username
            
            # Try other patterns
            patterns = [
                r'"name":"([^"]+)"',
                r'<strong>([^<]+)</strong>',
                r'>([^<]+)</a>'
            ]
            
            for pattern in patterns:
                matches = re.findall(pattern, response.text)
                for match in matches:
                    if (match and len(match.strip()) > 2 and 
                        'facebook' not in match.lower() and
                        'log' not in match.lower()):
                        return match.strip()
            
            return "Facebook User"
            
        except Exception:
            return "Facebook User"
    
    def extract_username(self, response):
        """Extract username from successful login response"""
        try:
            # Try multiple methods to get username
            patterns = [
                r'<title>([^<]+?)\s*\|\s*Facebook</title>',
                r'<title>([^<]+?)\s*-\s*Facebook</title>',
                r'"name":"([^"]+)"',
                r'data-gt=\'{"tn":"C"}\'>([^<]+)</a>',
                r'<strong[^>]*>([^<]+)</strong>'
            ]
            
            for pattern in patterns:
                match = re.search(pattern, response.text, re.IGNORECASE)
                if match:
                    username = match.group(1).strip()
                    # Clean up common suffixes
                    username = re.sub(r'\s*\|\s*Facebook.*$', '', username)
                    username = re.sub(r'\s*-\s*Facebook.*$', '', username)
                    if username and len(username) > 1:
                        return username
            
            # Fallback: try to get from profile page
            try:
                profile_response = self.session.get('https://mbasic.facebook.com/profile.php', timeout=10)
                for pattern in patterns:
                    match = re.search(pattern, profile_response.text, re.IGNORECASE)
                    if match:
                        username = match.group(1).strip()
                        username = re.sub(r'\s*\|\s*Facebook.*$', '', username)
                        if username and len(username) > 1:
                            return username
            except:
                pass
            
            return "Facebook User"
            
        except Exception:
            return "Facebook User"

def display_banner():
    """Display the tool banner"""
    banner_text = """
    ███████╗██████╗     ██╗      ██████╗  ██████╗ ██╗███╗   ██╗
    ██╔════╝██╔══██╗    ██║     ██╔═══██╗██╔════╝ ██║████╗  ██║
    █████╗  ██████╔╝    ██║     ██║   ██║██║  ███╗██║██╔██╗ ██║
    ██╔══╝  ██╔══██╗    ██║     ██║   ██║██║   ██║██║██║╚██╗██║
    ██║     ██████╔╝    ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║
    ╚═╝     ╚═════╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝
    """
    
    banner_panel = Panel(
        Align.center(Text(banner_text, style="bold blue")),
        title="[bold green]Facebook Login Tool[/bold green]",
        subtitle="[italic]Secure Terminal Authentication[/italic]",
        box=box.DOUBLE,
        style="cyan"
    )
    
    console.print(banner_panel)
    console.print()

def display_info():
    """Display tool information"""
    info_text = """
[bold green]✓[/bold green] Multiple login methods for better success rate
[bold green]✓[/bold green] Real Facebook authentication
[bold green]✓[/bold green] Secure credential handling
[bold green]✓[/bold green] Beautiful terminal interface
[bold green]✓[/bold green] Enhanced error detection

[bold yellow]Note:[/bold yellow] This tool tries 3 different methods to ensure successful login.
Your password is never stored and is only used for authentication.
    """
    
    info_panel = Panel(
        info_text,
        title="[bold cyan]Features[/bold cyan]",
        box=box.ROUNDED,
        style="white"
    )
    
    console.print(info_panel)
    console.print()

def get_credentials():
    """Get user credentials with beautiful UI"""
    console.print(Panel(
        "[bold yellow]Please enter your Facebook credentials[/bold yellow]",
        title="[bold blue]Login[/bold blue]",
        box=box.ROUNDED
    ))
    console.print()
    
    # Get email/username
    email = Prompt.ask("[bold cyan]Email/Username[/bold cyan]", console=console)
    
    # Get password (hidden input)
    console.print("[bold cyan]Password:[/bold cyan] ", end="")
    password = getpass("")
    
    return email, password

def show_loading(message):
    """Show loading spinner"""
    with console.status(f"[bold green]{message}[/bold green]", spinner="dots"):
        time.sleep(2)  # Simulate processing time

def display_success(username):
    """Display successful login"""
    success_text = f"""
[bold green]✅ LOGIN SUCCESSFUL![/bold green]

[bold white]Welcome, {username}![/bold white]

[green]Your Facebook account has been successfully authenticated.[/green]
[dim]Session established and verified.[/dim]
    """
    
    success_panel = Panel(
        Align.center(success_text),
        title="[bold green]Success[/bold green]",
        box=box.DOUBLE,
        style="green"
    )
    
    console.print(success_panel)

def display_error(error_message):
    """Display error message"""
    error_text = f"""
[bold red]❌ LOGIN FAILED[/bold red]

[red]{error_message}[/red]

[dim]Please check your credentials and try again.[/dim]
    """
    
    error_panel = Panel(
        Align.center(error_text),
        title="[bold red]Error[/bold red]",
        box=box.DOUBLE,
        style="red"
    )
    
    console.print(error_panel)

def main():
    """Main function"""
    try:
        # Clear screen
        os.system('clear' if os.name == 'posix' else 'cls')
        
        # Display banner and info
        display_banner()
        display_info()
        
        # Initialize Facebook login
        fb_login = FacebookLogin()
        
        while True:
            try:
                # Get credentials
                email, password = get_credentials()
                console.print()
                
                # Validate input
                if not email or not password:
                    console.print("[bold red]Please enter both email and password![/bold red]")
                    console.print()
                    continue
                
                # Show loading
                show_loading("Trying multiple authentication methods...")
                console.print()
                
                # Attempt login
                success, result = fb_login.login(email, password)
                
                if success:
                    display_success(result)
                    break
                else:
                    display_error(result)
                    console.print()
                    
                    # Ask if user wants to try again
                    try_again = Prompt.ask(
                        "[bold yellow]Would you like to try again?[/bold yellow]",
                        choices=["y", "n"],
                        default="y"
                    )
                    
                    if try_again.lower() == 'n':
                        console.print("[bold cyan]Goodbye![/bold cyan]")
                        break
                    
                    console.print()
                    
            except KeyboardInterrupt:
                console.print("\n[bold yellow]Operation cancelled by user.[/bold yellow]")
                break
            except Exception as e:
                console.print(f"[bold red]Unexpected error: {str(e)}[/bold red]")
                break
                
    except KeyboardInterrupt:
        console.print("\n[bold yellow]Goodbye![/bold yellow]")
    except Exception as e:
        console.print(f"[bold red]Fatal error: {str(e)}[/bold red]")

if __name__ == "__main__":
    main()
