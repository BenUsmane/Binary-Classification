import { useEffect } from "react"


function App () {
  useEffect(() =>{
  //   fetch('http://localhost:3000/api/predict', {
  //     method : "POST",
  //     headers : {
  //       "content-type " : "application/json"
  //   },
  //   body : JSON.stringify({
  //     "features": 
  //   })
  // })
  //     .then(res => res.json())
  //     .then(data => console.log(data))
  //     .catch(error => console.error('Error:', error))
  fetch('http://localhost:3000/api/')
    .then(res => res.text())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error))
    const data = {"features" : [5,3,2,3,4,5,4,3,2,5,5,3,2,3,4,5,4,3,2,5,5,3,2,3,4,5,4,3,2,5] }

    fetch("http://localhost:3000/api/predict/",{
      "method" : "POST",
      "headers" : {
        "content-type" : "application/json" 
      },
      "body" : JSON.stringify(data)
      
    })
    .then(res => res.text())
    .then(data => console.log(data))
    .catch(error => console.error("error happened ", error))
},[])
  return (
    <div>
      <form action="">
          <input type="text" name="name" placeholder="Enter your name" />
          <button type="submit">Submit</button>
      </form>
    </div>
  )
}

export default App