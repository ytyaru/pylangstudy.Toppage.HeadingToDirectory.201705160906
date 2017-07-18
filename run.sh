#eval "$(rbenv init -)"
#export PATH="~/.pyenv/bin:$PATH"
#eval "$(pyenv init -)"
#eval "$(pyenv virtualenv-init -)"

python3 Main.py
rbenv exec asciidoctor index.adoc
rbenv exec asciidoctor index_table.adoc

