{
  pkgs,
  ...
}:

{
  packages = with pkgs; [
    git
    gh-markdown-preview
  ];

  # https://devenv.sh/languages/
  languages.python = {
    enable = true;
    venv = {
      enable = true;
      requirements = ./requirements.txt;
    };
  };

  scripts.run.exec = ''
    python main.py
    xdg-open figure.png
  '';

  # https://devenv.sh/pre-commit-hooks/
  pre-commit.hooks = {
    black.enable = true;
  };
}
