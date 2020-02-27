#!/usr/bin/bash

# Simple Spotify Control
# Just call ./spotify_control --help

CMD="dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player"

case "$1" in
  "playpause" )
    ${CMD}.PlayPause
    exit $?
  ;;
  "next" )
    ${CMD}.Next
    exit $?
  ;;
  "previous" )
    ${CMD}.Previous
    exit $?
  ;;
  "stop" )
    ${CMD}.Stop
    exit $?
  ;;
  "play" )
    ${CMD}.Play
    exit $?
  ;;
  *)
    echo "Usage: $0 [command]"
    echo "  commands are: playpause, next, previous, stop, play"
    exit 1
  ;;
esac

