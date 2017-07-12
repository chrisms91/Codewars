//Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

// Stop gninnipS My sdroW!
// 6 Kyu

function spinWords(str){
  //TODO Have fun :)
  var wordArray = str.split(" ")
  
  for(var i=0; i<wordArray.length; i++){
    
    //if lengh of word is 5 and more, reverse word
    if(wordArray[i].length > 4){
      
      // empty array to store reversed word
      var reverse = [];
      
      for(var j=wordArray[i].length-1; j>=0; j--){
        
        //push into reverse array from the end of the character
        reverse.push(wordArray[i].charAt(j));
      }
      
      wordArray[i] = reverse.join("");
    }
  } 
  return wordArray.join(" ");
}