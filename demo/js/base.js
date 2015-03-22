

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

	}
}



function handleDragEnter(e) {
	e.preventDefault();
	e.target.classList.add("over");
	//e.target.style.backgroundColor = "white";
}


function handleDragStart(e) {
	
}



function handleDragLeave(e) {
	e.target.classList.remove("over");
}


function loadImages() {
	var list = document.querySelectorAll("#recommended-movies-list li");
	console.log(list[1]);

	for (var i = 0; i < list.length; i++) {
		var imageNum = i + 1;
		list[i].innerHTML = "<img src='images/" + imageNum +".jpg' >";
	}
}




















