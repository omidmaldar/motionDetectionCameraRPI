# Results 
* Prototype ran on 23 September 2019
* 56 videos captured automatically
  * Encoding: x.264, Saved as MKV
  * Dimension: 640 X 480
  * Bitrate: vary
  * Framerate: 25 frame/second
  * A number of videos are only 0, 1, 2, or 3 seconds. It's good to force the Motion to remove all the videos that are too short or are result of a false trigger.
* Total video size: ~120 MB
* Streaming rate over wifi was 50 
* Uptime was about ~6 hours. 
  * USB Camera consumes more power and drains the power bank faster.
* Approx. distance of the camera and the feeder: ~30cm

# Natural environment:
* Direction of sun beams during different hours of the day
  * If camera is facing the sun then at least the side of subject that is facing to camera  becomes very dark
* Temperature
  * The outside temperature was between 4-9 C
  * The board temperature was about ~40 C reported by `vcgencmd measure_temp` command
* Wind
  * causes lots of false trigger for recording videos e.g when branchs start to move
* Birds didn't trust the recorder station close to their feeder (power bank, Raspberr Pi, Usb cam which has 1m long cable)

# Camera better to  
 * be able to focus on the subject automatically.
 * be able to adjust the brightness automatically.
 * have a protective box form the rain, wind, sunshine and birds.
 * have zooming Lens
 * record in slow-motion mode.
   * Birds fly much faster than the framerate that the camera can capture
 * have night (low light) recording mode

# Question:
 * What kind of motions trigger video recording? and what are the criteria for stopping it or continuing it?
