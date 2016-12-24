app.controller('randomCtrl', function($scope, randomService){
    $scope.message = ' Hello Angular!'
    $scope.generateRandomNumber = function(){
        $scope.randomNumber = randomService.generate();
    };
});
