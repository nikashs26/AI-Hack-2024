import React, { useState } from "react";
import { useParams } from "react-router-dom";

function Page() {
    const title = useParams();
    const [carCount, setCarCount] = useState("");
    const [imageUrl, setImageUrl] = useState("");

    const requestOptions = {
        method: "GET",
        redirect: "follow"
      };

      const title_final = title.title.replace(/\s+/g, '').toLowerCase();
      
      fetch(`http://127.0.0.1:5001/${title_final}`, requestOptions)
        .then((response) => response.json())
        .then((result) => {
            setCarCount(result.car_count)
            setImageUrl(result.image_url)
        })
        .catch((error) => console.error(error));

    return (
        <div>
            <h1>Hello! {title.title}</h1>
            <p>{carCount}</p>
            <p>{imageUrl}</p>
        </div>
    )
}

export default Page;