/** @format */

const socket = io("/");
const whiteBoardImg = document.querySelector("#whiteBoardImg");
const video = document.querySelector("#myVideo");
const canvas = document.querySelector("#videoCanvas");
const context = canvas.getContext("2d");

const init = async () => {
	try {
		const stream = await getVideoStream();
		video.srcObject = stream;
        video.width = 1280;
        video.height = 720; 
		video.addEventListener("loadedmetadata", playVideo);
	} catch (e) {
		console.log(e);
		alert("Allow Mini Room to use your camera!");
	}
};

const playVideo = (e) => {
	e.target.play();
	canvas.width = e.target.width;
	canvas.height = e.target.height;
	setInterval(drawOnCanvas, 1000 / 6);
};

const drawOnCanvas = () => {
	context.drawImage(video, 0, 0, canvas.width, canvas.height);
	const image = canvas.toDataURL("image/jpeg");
	socket.emit("image", image);

	socket.on("processed-image", async (imgSrc) => {
		whiteBoardImg.setAttribute("src", imgSrc, 0.5);
	});
};

const getVideoStream = async () => {
	return await navigator.mediaDevices.getUserMedia({
		video: true,
	});
};

window.addEventListener("load", init);
