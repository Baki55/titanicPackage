GREEN		=	\e[92;5;118m
YELLOW		=	\e[93;5;226m
GREY		=	\e[33;2;37m
RESET		=	\e[0m
CURSIVE		=	\e[33;3m

PACKAGENAME = titanic
APINAME = titanicAPI
APPFILE = titanicApp

PYTHONVERSION = python3

ENVNAME = env

env:
		@$(PYTHONVERSION) -m venv $(ENVNAME)
		@printf "$(GREEN)	- Virtual env created.\n$(RESET)"

install:
		@printf "$(CURSIVE)$(GREY)	- Compiling $(PACKAGENAME)... $(RESET)\n"
		@pip install .
		@printf "$(GREEN)	- Package installed.\n$(RESET)"

api:
		@printf "$(CURSIVE)$(GREY)	- Running $(APINAME)... $(RESET)\n"
		@cd $(PACKAGENAME) && uvicorn $(APINAME):app

app:
		@printf "$(CURSIVE)$(GREY)	- Running $(APPNAME)... $(RESET)\n"
		@streamlit run $(PACKAGENAME)/$(APPFILE).py

uninstall:
		@pip uninstall $(PACKAGENAME).egg-info
		@printf "$(YELLOW)	- Package uninstalled.$(RESET)\n"


clean:
		@rm -rf $(PACKAGENAME).egg-info
		@printf "$(YELLOW)	- Package info deleted.$(RESET)\n"
		@rm -rf $(ENVNAME)
		@printf "$(YELLOW)	- Virtual env info deleted.$(RESET)\n"
		@rm -rf build
		@printf "$(YELLOW)	- build folder deleted.$(RESET)\n"