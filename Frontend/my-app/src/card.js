import React from "react";

function Card(title) {
    return(
        <div>
            <details>
                <summary>
                    {title}
                </summary>
        <div>
            <a href="/">{title}</a>
        </div> 
    </details>
    </div>
    )
}

export default Card;