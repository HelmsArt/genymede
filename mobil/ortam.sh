#!/bin/sh
# Build environment — stores no machine-specific paths, locates what exists. Loaded by the npm scripts;
# for manual use: . ./ortam.sh
if [ -z "$JAVA_HOME" ]; then
  for j in /opt/homebrew/opt/openjdk@21 /usr/local/opt/openjdk@21 "$(/usr/libexec/java_home -v 21 2>/dev/null)"; do
    [ -n "$j" ] && [ -d "$j" ] && export JAVA_HOME="$j" && break
  done
fi
if [ -z "$ANDROID_HOME" ]; then
  for a in "$ANDROID_SDK_ROOT" "$HOME/Library/Android/sdk" /opt/homebrew/share/android-commandlinetools "$HOME/Android/Sdk"; do
    [ -n "$a" ] && [ -d "$a" ] && export ANDROID_HOME="$a" && break
  done
fi
[ -n "$JAVA_HOME" ] && export PATH="$JAVA_HOME/bin:$PATH"
[ -n "$ANDROID_HOME" ] && export PATH="$ANDROID_HOME/platform-tools:$ANDROID_HOME/emulator:$PATH"
[ -z "$JAVA_HOME" ] && echo "WARNING: JDK 21 not found (brew install openjdk@21)" >&2
[ -z "$ANDROID_HOME" ] && echo "WARNING: Android SDK not found (brew install --cask android-commandlinetools)" >&2
:
