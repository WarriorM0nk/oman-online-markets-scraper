import colorama

def info(text, depth=0):
    if depth == 0:
        print(f'{colorama.Fore.CYAN}[i]{colorama.Fore.RESET} {text}')
    else:
        print('  ' * depth, f'{colorama.Fore.CYAN}[i]{colorama.Fore.RESET} {text}')

def success(text, depth=0):
    if depth == 0:
        print(f'{colorama.Fore.GREEN}[✓]{colorama.Fore.RESET} {text}')
    else:
        print('  ' * depth, f'{colorama.Fore.GREEN}[✓]{colorama.Fore.RESET} {text}')