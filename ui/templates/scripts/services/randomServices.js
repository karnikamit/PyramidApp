app.service('randomService', function(){
    var num = Math.floor(Math.random()*10);
    this.generate = function(){
        return num;
    };
});
