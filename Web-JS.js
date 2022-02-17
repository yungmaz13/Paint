var drawing=false;
const colours=["black","grey","white","red","yellow","pink","green","orange","violet","blue","aqua","lime"];
var colour=colours[0];
var [x,y]=[null,null];

const originalSploch=document.getElementById("originalSploch");

document.onmousemove=MouseFunction;
function MouseFunction(event){
	[x,y]=[event.clientX,event.clientY];
	document.getElementsByClassName("brush")[0].style.left=`${x}px`;
	document.getElementsByClassName("brush")[0].style.top=`${y}px`;
	return[x,y];
}

document.onmousedown=function(){drawing=true};
document.onmouseup=function(){drawing=false};

window.addEventListener("keydown",function(event){
	if(event.key=="c"){
		document.querySelectorAll('[id=sploch]').forEach(sploch=>sploch.remove());
	}
	else if(event.key=="z"){
		try{
			colour=colours[colours.indexOf(colour)+1];
		}catch{
			colour=colours[0];
		}
		document.getElementsByClassName("brush")[0].style.backgroundColor=colour;
	}
});

window.setInterval(function(event){
	if(drawing){
		let sploch=originalSploch.cloneNode(true);
		sploch.style.backgroundColor=colour;
		sploch.style.left=`${x}px`;
		sploch.style.top=`${y}px`;
		sploch.style.display="block";
		document.getElementsByTagName("main")[0].appendChild(sploch);
	}
},10);
