$(function load() {
    for (let i = 0; i < 10; i++) {
	$("body").append("<p class='container'></p>");
    }

    d3.selectAll("p.container").
	data([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).
	text(function(d) {return "number" + d; });
});
