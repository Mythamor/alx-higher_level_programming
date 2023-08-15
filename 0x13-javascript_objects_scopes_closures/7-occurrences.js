#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
	let count = 0;
	for (let l in list) {
		if (list[l] === searchElement) {
			count++;
		}
	}
	return count;
};
