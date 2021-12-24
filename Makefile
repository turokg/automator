PLIST_FILE ?= com.ek.mover.plist
PLIST_DIR ?= /Users/ek/Library/LaunchAgents
SCRIPT ?= /Users/ek/python/automator/main.py


all:
	@echo "deploy				- setup as a daemon on macos"
	@echo "stop				- remove daemon"
	@exit 0

deploy:
	launchctl unload $(PLIST_DIR)/$(PLIST_FILE)
	chmod +x $(SCRIPT)
	cp $(PLIST_FILE) $(PLIST_DIR)
	launchctl load $(PLIST_DIR)/$(PLIST_FILE)

stop:
	launchctl unload $(PLIST_DIR)/$(PLIST_FILE)


