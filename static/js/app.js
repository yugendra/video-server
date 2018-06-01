function playVideo() {
    var video_name = $("input[name=video]:checked").val();
    var video_folder = '/video/';
    var video_path = video_folder.concat(video_name);
    console.log(video_path)
    
    var videoplayer = document.getElementById('videoplayer');
    
    videoplayer.src = video_path
    videoplayer.play();
}