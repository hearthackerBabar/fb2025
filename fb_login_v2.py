#!/usr/bin/env python3
"""
Facebook Login Tool for Termux - Enhanced Version
A beautiful terminal-based Facebook login validator with improved reliability
"""

import requests
import re
import sys
import os
import json
import time
from getpass import getpass
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.align import Align
from rich import box
from urllib.parse import urlencode

console = Console()

class FacebookLoginV2:
    def __init__(self):
        self.session = requests.Session()
        self.base_headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1'
        }
        self.session.headers.update(self.base_headers)
    
    def login(self, email, password):
        """Enhanced Facebook login method"""
        try:
            # Method 1: Try basic mobile login
            success, result = self._try_basic_login(email, password)
            if success:
                return success, result
            
            # Method 2: Try alternative approach
            success, result = self._try_alternative_login(email, password)
            if success:
                return success, result
            
            # Method 3: Try with different user agent
            success, result = self._try_desktop_login(email, password)
            return success, result
            
        except Exception as e:
            return False, f"Login error: {str(e)}"
    
    def _try_basic_login(self, email, password):
        """Try basic mobile Facebook login"""
        try:
            # Get login page
            login_url = 'https://mbasic.facebook.com/login.php'
            response = self.session.get(login_url)
            
            if response.status_code != 200:
                return False, "Cannot access Facebook login page"
            
            # Extract form data
            form_data = self._extract_form_data(response.text)
            if not form_data:
                return False, "Cannot extract login form data"
            
            # Prepare login payload
            payload = {
                'email': email,
                'pass': password,
                'login': 'Log In',
                **form_data
            }
            
            # Set headers for POST request
            self.session.headers.update({
                'Referer': login_url,
                'Origin': 'https://mbasic.facebook.com',
                'Content-Type': 'application/x-www-form-urlencoded'
            })
            
            # Submit login
            post_url = 'https://mbasic.facebook.com/login/device-based/regular/login/'
            response = self.session.post(post_url, data=payload, allow_redirects=True, timeout=30)
            
            return self._check_login_response(response)
            
        except Exception as e:
            return False, f"Basic login failed: {str(e)}"
    
    def _try_alternative_login(self, email, password):
        """Try alternative login method"""
        try:
            # Use different endpoint
            login_url = 'https://www.facebook.com/login.php'
            
            # Update headers for desktop-like request
            self.session.headers.update({
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            })
            
            response = self.session.get(login_url)
            
            if response.status_code != 200:
                return False, "Cannot access alternative login page"
            
            # Extract form data
            form_data = self._extract_form_data(response.text)
            
            payload = {
                'email': email,
                'pass': password,
                **form_data
            }
            
            # Submit login
            response = self.session.post(login_url, data=payload, allow_redirects=True, timeout=30)
            
            return self._check_login_response(response)
            
        except Exception as e:
            return False, f"Alternative login failed: {str(e)}"
    
    def _try_desktop_login(self, email, password):
        """Try desktop Facebook login as last resort"""
        try:
            # Reset session with desktop headers
            self.session = requests.Session()
            self.session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive'
            })
            
            # Get desktop login page
            login_url = 'https://www.facebook.com/'
            response = self.session.get(login_url)
            
            if response.status_code != 200:
                return False, "Cannot access Facebook"
            
            # Extract form data
            form_data = self._extract_form_data(response.text)
            
            payload = {
                'email': email,
                'pass': password,
                **form_data
            }
            
            # Submit login
            post_url = 'https://www.facebook.com/login/device-based/regular/login/'
            response = self.session.post(post_url, data=payload, allow_redirects=True, timeout=30)
            
            return self._check_login_response(response)
            
        except Exception as e:
            return False, f"Desktop login failed: {str(e)}"
    
    def _extract_form_data(self, html):
        """Extract form data from HTML"""
        try:
            form_data = {}
            
            # Common patterns for Facebook form fields
            patterns = {
                'lsd': [r'name="lsd" value="([^"]*)"', r'"LSD",\[],\{"token":"([^"]*)"', r'"lsd":"([^"]*)"'],
                'jazoest': [r'name="jazoest" value="([^"]*)"', r'"jazoest":"([^"]*)"'],
                'm_ts': [r'name="m_ts" value="([^"]*)"'],
                'li': [r'name="li" value="([^"]*)"'],
                'try_number': [r'name="try_number" value="([^"]*)"'],
                'unrecognized_tries': [r'name="unrecognized_tries" value="([^"]*)"'],
                'bi_xrwh': [r'name="bi_xrwh" value="([^"]*)"'],
                '__a': [r'name="__a" value="([^"]*)"'],
                '__req': [r'name="__req" value="([^"]*)"'],
                'fb_dtsg': [r'name="fb_dtsg" value="([^"]*)"', r'"fb_dtsg":"([^"]*)"']
            }
            
            for field, pattern_list in patterns.items():
                for pattern in pattern_list:
                    match = re.search(pattern, html)
                    if match:
                        form_data[field] = match.group(1)
                        break
                else:
                    form_data[field] = ''
            
            return form_data
            
        except Exception:
            return {}
    
    def _check_login_response(self, response):
        """Check if login was successful"""
        try:
            url = response.url.lower()
            text = response.text.lower()
            
            # Success indicators
            success_patterns = [
                'home.php' in url,
                'facebook.com/home' in url,
                'mbasic.facebook.com/home' in url,
                '/home.php' in url,
                'welcome' in text and 'facebook' in text,
                'newsfeed' in text,
                'timeline' in text and 'facebook' in text
            ]
            
            if any(success_patterns):
                username = self._extract_username(response)
                return True, username
            
            # Error patterns
            error_patterns = {
                'checkpoint': 'Account requires verification (2FA enabled)',
                'login_attempt' in url: 'Incorrect username or password',
                'login.php' in url: 'Login failed - check credentials',
                'captcha' in text: 'Captcha verification required',
                'blocked' in text: 'Account temporarily restricted',
                'disabled' in text: 'Account disabled',
                'suspended' in text: 'Account suspended',
                'error' in text: 'Login error occurred'
            }
            
            for pattern, message in error_patterns.items():
                if (isinstance(pattern, str) and pattern in url) or (isinstance(pattern, str) and pattern in text) or (isinstance(pattern, bool) and pattern):
                    return False, message
            
            return False, "Login failed - please verify your credentials"
            
        except Exception as e:
            return False, f"Response check failed: {str(e)}"
    
    def _extract_username(self, response):
        """Extract username from response"""
        try:
            # Multiple patterns to find username
            patterns = [
                r'<title>([^<|]+?)(?:\s*\|\s*Facebook|\s*-\s*Facebook)</title>',
                r'"name":"([^"]+)"',
                r'<a[^>]*href="[^"]*profile\.php[^"]*"[^>]*>([^<]+)</a>',
                r'<span[^>]*class="[^"]*"[^>]*>([^<]+)</span>',
                r'data-overviewsection="contact_basic">([^<]+)</div>'
            ]
            
            for pattern in patterns:
                matches = re.findall(pattern, response.text, re.IGNORECASE)
                for match in matches:
                    username = match.strip()
                    # Filter out common false positives
                    if (username and 
                        len(username) > 1 and 
                        'facebook' not in username.lower() and
                        'log in' not in username.lower() and
                        'sign up' not in username.lower() and
                        not username.isdigit()):
                        return username
            
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
        title="[bold green]Facebook Login Tool V2[/bold green]",
        subtitle="[italic]Enhanced Authentication[/italic]",
        box=box.DOUBLE,
        style="cyan"
    )
    
    console.print(banner_panel)
    console.print()

def display_info():
    """Display tool information"""
    info_text = """
[bold green]✓[/bold green] Multiple login methods for better success rate
[bold green]✓[/bold green] Enhanced error detection and handling
[bold green]✓[/bold green] Real Facebook authentication
[bold green]✓[/bold green] Beautiful terminal interface

[bold yellow]Note:[/bold yellow] This tool tries multiple methods to ensure successful login.
    """
    
    info_panel = Panel(
        info_text,
        title="[bold cyan]Enhanced Features[/bold cyan]",
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
        time.sleep(1.5)

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
        fb_login = FacebookLoginV2()
        
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
