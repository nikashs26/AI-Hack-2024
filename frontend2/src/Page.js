import React, { useState } from "react";
import { useParams } from "react-router-dom";

function Page() {
    const title = useParams();
    const [carCount, setCarCount] = useState("");
    const [imageUrl, setImageUrl] = useState("");
    const [emptySpots, setEmptySpots] = useState("");


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
            setEmptySpots(result.empty_spots)
        })
        .catch((error) => console.error(error));

    return (
        <div>
            <h1>Results for {title.title}</h1>
            <h3>car count</h3><p>{carCount}</p>
            <h3>image url</h3><p>{imageUrl}</p>
            <h3>emptySpots</h3><p>{emptySpots - carCount}</p>
        </div>
    )
}

export default Page;