// Directions Reduction
// Level: 5 Kyu

/* Task

  Write a function dirReduc which will take an array of strings and returns an array of strings 
  with the needless directions removed (W<->E or S<->N side by side). */


function dirReduc(arr){
  var index = 0;
  
  while(index < arr.length){
    if( (arr[index] === "NORTH" && arr[index+1] === "SOUTH") ||
        (arr[index] === "SOUTH" && arr[index+1] === "NORTH") ||
        (arr[index] === "WEST" && arr[index+1] === "EAST") ||
        (arr[index] === "EAST" && arr[index+1] === "WEST") ){
        
      arr.splice(index, 2);
      console.log("index: " + index);
      index--;
    }
    else{
      index++;
    }
  }
 return arr;
}
