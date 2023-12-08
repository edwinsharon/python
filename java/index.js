// function asfd()
//     {
//       alert("you are in danger")
//     }
// document.getElementById('a').addEventListener('change',(e)=>{
//   console.log(e.target.value);
// })
document.getElementById('get').addEventListener('click',()=>{
  let fno=parseInt(document.getElementById('fno').value)
  let sno=parseInt(document.getElementById('sno').value)
  x=fno+sno
  const refer = document.getElementById('res')
  refer.innerText = x
})