function randint(min,max) {
	return Math.floor(Math.random() * (max - min + 1)) + min;
}

	
function displayNum() {
	let a, b;
	a = randint(1,98); b = randint(a+1,99);
	document.getElementById("question").innerText = a + "/" + b + "=";

}
