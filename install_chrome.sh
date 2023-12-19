#!/bin/bash
# setup.sh

# Exit on error
set -o errexit

# Storage directory for Chrome
STORAGE_DIR=/opt/render/project/.render

# Check if Chrome is already downloaded
if [[ ! -d $STORAGE_DIR/chrome ]]; then
  echo "...Downloading Chrome"
  mkdir -p $STORAGE_DIR/chrome

  # Download Chrome for Linux
  cd $STORAGE_DIR/chrome
  wget -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  dpkg -x ./google-chrome-stable_current_amd64.deb $STORAGE_DIR/chrome
  rm ./google-chrome-stable_current_amd64.deb
  cd $HOME/project/src  # Make sure we return to where we were

else
  echo "...Using Chrome from cache"
fi

# Provide additional instructions or setup steps
echo "Chrome has been downloaded and installed. You can now proceed with your project setup."

# Add any additional steps or instructions here
# ...

# End of setup.sh
