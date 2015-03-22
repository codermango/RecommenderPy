

function startLoad() {
	loadImages();
	setDragTrueAndAddEvent();
}

// 以下为页面加载时，给相应标签加上drag属性和事件
function setDragTrueAndAddEvent() {
	
	var recommendedLiList = document.getElementById("recommended-movies-list").getElementsByTagName("li");
	var likedMovieLiList = document.getElementById("liked-movies-list").getElementsByTagName("li");

	for (var i = 0; i < recommendedLiList.length; i++) {
		// 1. 给recommended-movies里地li加上drappable="true"
		recommendedLiList[i].draggable = "true";

		// 2. 给recommende-movies里地li加上ondragstart函数
		recommendedLiList[i].addEventListener("dragstart", function() {handleDragStart(event);});
	}

	for (var i = 0; i < likedMovieLiList.length; i++) {
		// 3. 给drop-buckets里地li加上ondragenter和ondrop函数
		likedMovieLiList[i].addEventListener("dragenter", function() {handleDragEnter(event);});
		likedMovieLiList[i].addEventListener("dragleave", function() {handleDragLeave(event);});

		likedMovieLiList[i].addEventListener("drop", function() {handleDrop(event);});
		likedMovieLiList[i].addEventListener("dragover", function() {handleDragOver(event);}, false);
	}
}

function handleDragOver(e) {
	e.preventDefault();
}

function handleDragEnter(e) {
	e.preventDefault();
	e.target.classList.add("over");
	//e.target.style.backgroundColor = "white";
}


function handleDragStart(e) {
	dragSource = e.target;
	e.dataTransfer.setData("imgPath", e.target.src);
	//console.log(e.target.src);
}


function handleDragLeave(e) {

	e.target.classList.remove("over");
}

function handleDrop(e) {
	e.preventDefault();
	targetEle = e.target;
	targetEle.classList.remove("over");
	var childNodes = targetEle.childNodes;
	console.log(childNodes.length);

	if (childNodes.length == 0) {
		var imgPath = e.dataTransfer.getData("imgPath");
		targetEle.innerHTML = "<img src='" + imgPath + "' >";
		console.log(targetEle.innerHTML);
	}


}


// 网页初始的时候加载网页
function loadImages() {
	var ulElement = document.querySelector("#recommended-movies-list");
	console.log(ulElement);
	for (var i = 0; i < 10; i++) {
		var liElement = document.createElement("li");
		var imgElement = document.createElement("img");
		imgElement.src = "images/" + i + ".jpg";
		liElement.appendChild(imgElement);
		ulElement.appendChild(liElement);
	}
}




















