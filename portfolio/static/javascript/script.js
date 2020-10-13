// 2. This code loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// 3. This function creates an <iframe> (and YouTube player)
//    after the API code downloads.
var player;
function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
        height: '360',
        width: '640',
        videoId: '',
        playerVars: { 'disablekb': 0 },
        events: {
            'onReady': onPlayerReady,
            'onReady': loadPlaylist_playlist_id,
            'onStateChange': onPlayerStateChange
        }
    });
}

// 4. The API will call this function when the video player is ready.
function onPlayerReady(event) {
    event.target.setVolume(30);
}

// 5. The API calls this function when the player's state changes.
//    The function indicates that when playing a video (state=1),
//    the player should play for six seconds and then stop.
var done = false;
function onPlayerStateChange(event) {
    if (event.data == YT.PlayerState.PLAYING) {
        setPlaying(true);
    } else if (event.data == YT.PlayerState.PAUSED) {
        setPlaying(false);
    }
}

function controller() {
    if (player.getPlayerState() == 1) {
        player.pauseVideo();
    }
    else {
        player.playVideo();
    }
}

function loadPlaylist_playlist_id() {
    player.loadPlaylist({
        'list': 'PL2HEDIx6Li8jGsqCiXUq9fzCqpH99qqHV',
        'listType': 'playlist',
        'index': 0,
        'startSeconds': 0,
        'suggestedQuality': 'large'
    });
}

function title() {
    player.getVideoData().title;
}


