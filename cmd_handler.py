CMD_FUNCTIONS = {
    "help": help
}

def handle(command, COMMANDS):
    if command in COMMANDS and command not in CMD_FUNCTIONS:
        raise ValueError("Config file contains unsupported command")

    # 'help' command is the only command that needs knowledge of other commands
    if command == 'help':
        return help(COMMANDS)

    if command in COMMANDS and command in CMD_FUNCTIONS:
        return CMD_FUNCTIONS[command]

    return ''

def help(COMMANDS):
    cmd_statements = [ 'Thread tracker for forums\n' ]

    for cmd in COMMANDS:
        cmd_statement = '**{}** - {}'.format(cmd, COMMANDS[cmd])
        cmd_statements.append(cmd_statement)

    help_statement = '\n'.join(cmd_statements)
    return help_statement