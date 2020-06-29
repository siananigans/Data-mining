# Git Hooks

Use the script from https://github.com/icefox/git-hooks to install/execute them.

tl;dr:

```bash
# install script
sudo curl -o /usr/local/bin/git-hooks https://raw.githubusercontent.com/icefox/git-hooks/master/git-hooks
sudo chmod +x /usr/local/bin/git-hooks

# install hooks per-repo
cd your-repo
git-hooks --install
```

## Bypassing

Please use with care.

`git commit --no-verify`
