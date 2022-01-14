var unsaved = false;
var outputData = {};
const CRITERIA = ["factual", "coherent", "fluent"];

function evaluateSentences(dataObj) {
	let div = document.getElementById('summaries-div');
	$("#chart-img").attr("src", "");
	$("#chart-title").text("");
	$("#chart-question").text("");
	div.innerHTML = "";

	if (dataObj == null) {
		$("#chart-img").attr("src", "imgs/loading.gif");
		div.innerHTML = `<h2 class="ui red header">Error: Invalid chart number.</h2><br>`;
		return;
	}
	
	// Title
	$("#chart-title").text(dataObj["title"]);

	// Image
	$("#chart-img").attr("src", dataObj["img"]);

	// Question
	$("#chart-question").text(dataObj["question"]);

	// Summaries
	for (let i = 0; i < 2; i++) {
		let key = dataObj[`Summary ${i + 1}`];
		
		let header = document.createElement("h3");
		header.innerText = `Answer #${i + 1}`;

		let caption = document.createElement("div");
		caption.className = `ui segment`;
		caption.innerText = dataObj[key];

		div.appendChild(header);
		div.appendChild(caption);
	}

	// Evaluation
	$('input[type="radio"]:checked').prop("checked", false);
	if (dataObj.number in outputData) {
		// console.log(dataObj.number);
		// console.log(outputData);
		let outputObj = outputData[dataObj.number];
		CRITERIA.forEach(criterion => {
			$(`#${criterion}-${outputObj[criterion]}`).prop("checked", true);
		});
	}
};

function generateOutputCsv() {
	let csvContent = "data:text/csv;charset=utf-8,";

	const columns = ["number", "id", ...CRITERIA];
	csvContent += columns.join(",") + "\r\n";

	let outputArr = Object.keys(outputData).map(number => {
		let rowObj = {
			number,
			...outputData[number],
		};
		let rowArr = columns.map(column => column in rowObj ? rowObj[column] : "");

		return rowArr;
	});

	outputArr.sort((firstEl, secondEl) => firstEl[0] - secondEl[0]);

	outputArr.forEach(rowArr => {
		// console.log(rowArr);
		let row = rowArr.join(",");
		csvContent += row + "\r\n";
	});

	return encodeURI(csvContent);
}

$(function () {
	$("#instructions-btn").click(function () {
		$("#instructions-modal").modal('show');
	});

	$('.menu .item').tab();

	$("#upload-input").change(e => {
		let el = $(e.target);
		let regex = /^([a-zA-Z0-9\s_\\.\-:\)\()])+(.csv)$/;

		if (regex.test(el.val().toLowerCase())) {
			let reader = new FileReader();

			reader.addEventListener("load", () => {
				d3.csvParse(reader.result, row => {
					const {
						number,
						...rest
					} = row;
					outputData[number] = rest;
				})

				let maxChartNum = Math.max.apply(null, Object.keys(outputData));
				if (maxChartNum >= 0) {
					$("#chart-num").val(maxChartNum + 1);
					$("#chart-num").trigger("change");
				}
			});

			reader.readAsText(el[0].files[0]);

		} else {
			alert("Please upload a valid CSV file!");
		}
	});

	d3.csv("outputs/combined.csv").then(annotData => {
		$("#chart-num").on("change input", e => {
			let i = $(e.target).val();
			evaluateSentences(annotData[i]);
		});

		$("#chart-num").attr("max", annotData.length - 1);
		$("#chart-num").trigger("change");

		$("form").submit(function (e) {
			e.preventDefault();

			// Update annotations
			let annotArr = $(e.target).serializeArray();
			let annotObj = {};

			annotArr.forEach(row => {
				let criterion = row["name"];
				let value = row["value"].split("-")[1];
				annotObj[criterion] = value;
			});

			let number = parseInt($("#chart-num").val());

			outputData[number] = {
				id: annotData[number].id,
				...annotObj,
			};
			
			$('input[type="radio"]:checked').prop("checked", false);

			$("#chart-num").val(number + 1);
			$("#chart-num").trigger("change");

			unsaved = true;
		});

		$("#download-btn").click(e => {
			e.preventDefault();

			let outputCsv = generateOutputCsv();
			let el = $("#real-download-btn");
			el.attr("href", outputCsv);
			el[0].click();

			unsaved = false;
		});
	});
});


window.onbeforeunload = () => {
	if (unsaved) {
		return "You have unsaved changes on this page. Do you want to leave this page and discard your changes or stay on this page?";
	}
};
