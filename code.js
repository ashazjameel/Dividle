function randint(min,max) {
	return Math.floor(Math.random() * (max - min + 1)) + min;
}

	
function displayNum() {
	let a, b;
	a = randint(1,98); b = randint(a+1,99);
	document.getElementById("question").innerText = a + "/" + b + " =";
}

function correct(c){
	document.getElementById("answer").innerText = c;
	document.getElementById("answer").style.color = "green";
}

function check(num) {
	let a, b, c, txt, ind, ans, nextDig;
	txt = document.getElementById("question").innerText;
	ind = txt.indexOf("/");
	a = txt.slice(0,ind); b = txt.slice(ind+1,-2); c = (a/b).toString();
	ans = document.getElementById("answer").innerText.slice(2,-1);
	if (ans.length + 2 == c.length) {
		return;		//win
	}
	nextDig = c[2+ans.length];
	if (num == nextDig) {
		document.getElementById("answer").innerText = c.slice(0,3+ans.length)+"_";		//correct
	} else {
		return;		//incorrect
	}
}


