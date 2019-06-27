var SetTime=5;
function msg_time(){
	
	var msg = "남은 시간 " + SetTime ;
	document.all.ViewTimer.innerHTML = msg;
	SetTime--;
	if(SetTime <0){
		clearInterval(tid);
		}
	}	
	window.onload = function TimerStart(){tid = setInterval('msg_time()',1000)};


