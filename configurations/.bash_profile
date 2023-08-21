# Configuración de path
export PATH=/opt/homebrew/bin:$PATH

# Autocompletado de git
source ~/git-completion.bash
source ~/git-prompt.sh
export GIT_PS1_SHOWDIRTYSTATE=1

# Texto del PS1
export PS1='\[\e[32m\]\u@macbook \[\e[34m\]\W\[\033[31m\]$(__git_ps1 " (%s)")\[\e[m\] '

# Autocompletado de ssh
_complete_ssh_hosts ()
{
        COMPREPLY=()
        cur="${COMP_WORDS[COMP_CWORD]}"
        comp_ssh_hosts=`cat ~/.ssh/known_hosts | \
                        cut -f 1 -d ' ' | \
                         sed -e s/,.*//g | \
                         grep -v ^# | \
                         uniq | \
                         grep -v "\[" ;
                         cat ~/.ssh/config | \
                         grep --color=never "^Host " | \
                         awk '{print $2}'
                   `
        COMPREPLY=( $(compgen -W "${comp_ssh_hosts}" -- $cur))
        return 0
}
complete -F _complete_ssh_hosts ssh


# Jetbrains Toolbox
export PATH="$PATH:/Users/USERNAME/Library/Application Support/JetBrains/Toolbox/scripts"

# VSCode
export PATH="$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"

# Python
export PATH="$PATH:/Users/USERNAME/Library/Python/3.8/bin"

# Local bin
export PATH="$PATH:/usr/local/bin"

# Node
export PATH="$PATH:${HOME}/.npm-packages/bin"
export PATH="$PATH:${HOME}/.npm-global/bin/"


# Load Angular CLI autocompletion.
source <(ng completion script)