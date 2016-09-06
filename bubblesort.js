function bubbleSort(arr) {
	var arrLimit = arr.length;
	var temp = 0;
		while (arrLimit != 0) {
			for (var i = 0; i < arrLimit; i++) {
				if (arr[i]>arr[i+1]) {
					temp = arr [i+1];
					arr[i+1] = arr[i];
					arr[i] = temp;
					//console.log(i,arrLimit);
					//console.log(arr);
				}
				else {
					//console.log(i,arrLimit);
					//console.log(arr);
				}
			};
			arrLimit --;
		};
	return arr;
}

function generate(amount) {
	var  mylist  = [];
	for (var i = 0; i < amount;  i++) {
		mylist.push(Math.random()*10000)
	}
	return  mylist;
}

var mylist = generate(1000);
console.log(bubbleSort(mylist));
