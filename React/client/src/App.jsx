import { useEffect } from "react";
import {
  FaLeaf,
  FaSpaceShuttle,
  FaDiagnoses,
  FaToolbox,
  FaChartPie,
  FaPowerOff,
} from "react-icons/fa";

function App() {
  useEffect(() => {
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
    fetch("http://localhost:3000/api/")
      .then((res) => res.text())
      .then((data) => console.log(data))
      .catch((error) => console.error("Error:", error));
    const data = {
      features: [
        5, 3, 2, 3, 4, 5, 4, 3, 2, 5, 5, 3, 2, 3, 4, 5, 4, 3, 2, 5, 5, 3, 2, 3,
        4, 5, 4, 3, 2, 5,
      ],
    };

    fetch("http://localhost:3000/api/predict/", {
      method: "POST",
      headers: {
        "content-type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((res) => res.text())
      .then((data) => console.log(data))
      .catch((error) => console.error("error happened ", error));
  }, []);
  return (
    <div className="flex">
      <div className="bg-blue-200 h-screen w-1/5 rounded-2xL pl-8">
        <div className="pt-6 text-2xl font-bold text-gray-700">
          <FaLeaf className="text-green-400" />
          <span>Agrismart</span>
          <div className="text-sm font-light">Admin</div>
        </div>
        <div className="mt-20">
          <div className="text-2xl font-semibold mb-10 ">
            <div className="inline-flex">
              <FaChartPie />
              Dashboard
            </div>
          </div>
          <div className="text-2xl font-semibold mb-10 ">
            <div className="inline-flex">Parcelle</div>
          </div>
          <div className="text-2xl font-semibold mb-10 ">
            <div className="inline-flex">Assistant</div>
          </div>
          <div className="text-2xl font-semibold mb-10 inline-flex">
            <FaDiagnoses />
            Diagnostic
          </div>
          <div className="text-2xl font-semibold mb-10 inline-flex">
            {" "}
            <FaToolbox /> More Tools
          </div>
        </div>
        <div>
          <div className="text-2xl font-semibold mt-16 bg-blue-400 inline-flex p-4 rounded-2xl">
          
            <div className="inline-flex">
              {" "}
              <FaPowerOff className="mr-4" /> Logout
            </div>
          </div>
        </div>
      </div>
      <div className="bg-gray-200 w-4/5 flex flex-col  ">
        <div className="h-24 bg-blue-400">Header</div>
        Main Content
      </div>
    </div>
  );
}

export default App;
