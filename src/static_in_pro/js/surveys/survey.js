(function(){
	'use strict';
	angular.module('survey',['ngRoute'])
		.controller('SurveyController', ['$scope', '$http', SurveyController]);
		

	function SurveyController($scope, $http) {
		$scope.add = function (list, title, description) {
			var question = {
				// title:title,
				// list:list.id,
				
				// description:description

				survey: survey.id,
				question: question,
				style: style,
				order: order,
			};
			$http.post('/surveys/questions/', card)
				.then(function(response){
					survey.question.push(response.data);
				},
				function(){
					alert('could not create card');
				});
		};

		$scope.data = [];
		$http.get('surveys/api/surveys/').then(function(response){
			$scope.data = response.data;
			console.log(response.data);
			console.log(response);
		});
	}
}());
