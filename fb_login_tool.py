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
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
    
    def get_login_form_data(self):
        """Get the login form data from Facebook's mobile login page"""
        try:
            url = 'https://m.facebook.com/login.php'
            response = self.session.get(url)
            
            # Extract necessary form data
            lsd = re.search(r'name="lsd" value="([^"]*)"', response.text)
            jazoest = re.search(r'name="jazoest" value="([^"]*)"', response.text)
            m_ts = re.search(r'name="m_ts" value="([^"]*)"', response.text)
            li = re.search(r'name="li" value="([^"]*)"', response.text)
            
            form_data = {
                'lsd': lsd.group(1) if lsd else '',
                'jazoest': jazoest.group(1) if jazoest else '',
                'm_ts': m_ts.group(1) if m_ts else '',
                'li': li.group(1) if li else '',
                'try_number': '0',
                'unrecognized_tries': '0',
                'bi_xrwh': '0'
            }
            
            return form_data
        except Exception as e:
            console.print(f"[red]Error getting form data: {str(e)}[/red]")
            return None
    
    def login(self, email, password):
        """Attempt to login to Facebook"""
        try:
            # Get initial form data
            form_data = self.get_login_form_data()
            if not form_data:
                return False, "Failed to get login form data"
            
            # Add credentials to form data
            form_data.update({
                'email': email,
                'pass': password,
                'login': 'Log In'
            })
            
            # Submit login form
            login_url = 'https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100'
            response = self.session.post(login_url, data=form_data, allow_redirects=True)
            
            # Check if login was successful
            if 'home.php' in response.url or 'facebook.com/?sk=h_chr' in response.url:
                # Get user's name from the page
                name_match = re.search(r'<title>([^<]+)</title>', response.text)
                if name_match:
                    username = name_match.group(1).replace(' | Facebook', '').strip()
                else:
                    # Try alternative method to get username
                    profile_url = 'https://m.facebook.com/profile.php'
                    profile_response = self.session.get(profile_url)
                    name_match = re.search(r'<title>([^<]+)</title>', profile_response.text)
                    username = name_match.group(1).replace(' | Facebook', '').strip() if name_match else "User"
                
                return True, username
            
            elif 'checkpoint' in response.url:
                return False, "Account requires verification (checkpoint)"
            elif 'login_attempt' in response.url or 'login.php' in response.url:
                return False, "Incorrect username or password"
            else:
                return False, "Login failed - unknown error"
                
        except requests.exceptions.RequestException as e:
            return False, f"Network error: {str(e)}"
        except Exception as e:
            return False, f"Unexpected error: {str(e)}"

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
[bold green]✓[/bold green] Real Facebook authentication
[bold green]✓[/bold green] Secure credential handling
[bold green]✓[/bold green] Beautiful terminal interface
[bold green]✓[/bold green] Error handling & validation

[bold yellow]Note:[/bold yellow] This tool validates your credentials with Facebook's servers.
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
                show_loading("Authenticating with Facebook...")
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
