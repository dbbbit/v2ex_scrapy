db = connect("localhost:27017/v2ex");
for(var i = 1; i < db.member.count(); i++){
    var res = db.member.count({_id:i})
    if(!res)print(i)
}
