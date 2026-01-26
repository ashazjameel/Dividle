function randint(min,max) {
	return Math.floor(Math.random() * (max - min + 1)) + min;
}

	
function displayNum() {
	let a, b;
	a = randint(1,98); b = randint(a+1,99);
	document.getElementById("question").innerText = a + "/" + b + " =";
	document.getElementById("answer").innerText = "0._";
	document.getElementById("answer").style.color = "#000000";
}

function correct(c){
	document.getElementById("answer").innerText = c;
	document.getElementById("answer").style.color = "#00FF00";
	window.setTimeout(displayNum,750);
}

function check(num) {
	let a, b, c, txt, ind, ans, nextDig;
	txt = document.getElementById("question").innerText;
	ind = txt.indexOf("/");
	a = txt.slice(0,ind); b = txt.slice(ind+1,-2); c = (a/b).toString();
	ans = document.getElementById("answer").innerText;
	
	if (ans.slice(-1) != "_") {
		return;			//already won
	}
	
	ans = ans.slice(2,-1);
	nextDig = c[2+ans.length];
	if (num == nextDig) {
		document.getElementById("answer").innerText = c.slice(0,3+ans.length)+"_";		//correct
		if (ans.length + 3 == c.length) {
			correct(c);		//win
			return;
		}
	} else {
		return;		//incorrect
	}
}






