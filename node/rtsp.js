const Stream = require('node-rtsp-stream');

stream = new Stream({
  name: 'foscam_stream',
  streamUrl: 'rtsp://210.99.70.120:1935/live/cctv001.stream',
  wsPort: 1935, // 웹소켓을 통한 스트림 서비스 포트
  ffmpegOptions: { // options ffmpeg flags
    '-stats': '', // an option with no neccessary value uses a blank string
    '-force_fps': 60 // options with required values specify the value after the key, 30:blur있음
  }
});