(function(){
	'use strict';
	angular.module('survey',['ngRoute'])
		.controller('SurveyController', ['$scope', '$http', SurveyController]);
		

	function SurveyController($scope, $http) {
		$scope.add = function (survey, question, style, order) {
			var question = {

				survey: survey.id,
				question: question,
				style: style,
				order: order,
			};
			$http.post('/surveys/questions_api/', question)
				.then(function(response){
					survey.question.push(response.data);
				},
				function(){
					alert('could not create card');
				});
		};

		$scope.data = [];
		$http.get('/surveys/surveys_api/').then(function(response){
			$scope.data = response.data;
			console.log(response.data);
			console.log(response);
		});
	}
}());
