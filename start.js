require('fs').readFileSync('token.txt', 'utf-8').split(/\r?\n/).forEach(function(line){
  console.log(line);
})