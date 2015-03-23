

function startLoad() {
	loadImages();
	setDragTrueAndAddEvent();
}

// 以下为页面加载时，给相应标签加上drag属性和事件
function setDragTrueAndAddEvent() {

    var recommendedImgList = document.querySelectorAll("#recommended-movies-list li img");
    var likedMovieLiList = document.querySelectorAll("#liked-movies-list li");


	for (var i = 0; i < recommendedImgList.length; i++) {
		// 1. 给recommended-movies里地li加上drappable="true"
		recommendedImgList[i].draggable = "true";

		// 2. 给recommende-movies里地li加上ondragstart函数
		recommendedImgList[i].addEventListener("dragstart", function() {handleDragStart(event);}, false);
	}

	for (var i = 0; i < likedMovieLiList.length; i++) {
		// 3. 给drop-buckets里地li加上ondragenter和ondrop函数
		likedMovieLiList[i].addEventListener("dragenter", function() {handleDragEnter(event);}, false);
        likedMovieLiList[i].addEventListener("dragover", function() {handleDragOver(event);}, false);
		likedMovieLiList[i].addEventListener("dragleave", function() {handleDragLeave(event);}, false);
		likedMovieLiList[i].addEventListener("drop", function() {handleDrop(event);}, false);
        likedMovieLiList[i].addEventListener("dragend", function() {handleDragEnd(event);}, false);
		
        console.log(likedMovieLiList[i].innerHTML + 'aaa');
	}
}


function handleDragStart(e) {
    e.dataTransfer.setData("imgPath", e.target.src);
    //console.log(e.target.src);
}


function handleDragOver(e) {
	e.preventDefault();
    e.dataTransfer.dropEffect = 'move';
    return false;
}

function handleDragEnter(e) {
	e.target.classList.add("over");
	//e.target.style.backgroundColor = "white";
}


function handleDragLeave(e) {
	e.target.classList.remove("over");
}

function handleDrop(e) {
	e.stopPropagation();
	targetEle = e.target;
	targetEle.classList.remove("over");
	var childNodes = targetEle.childNodes;
	//console.log(childNodes.length);

	if (childNodes.length == 0) {
		var imgPath = e.dataTransfer.getData("imgPath");
		targetEle.innerHTML = "<img src='" + imgPath + "' >";
		//console.log(targetEle.innerHTML);
	}

    return false;
}


function handleDragEnd(e) {
    e.target.classList.remove("over");
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




















