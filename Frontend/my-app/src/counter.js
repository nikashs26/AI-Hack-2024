import React from "react";

function counter()
{
    const [count, setCount] = React.usedState(0)

    function handleCount()
    {
        setCount[count+1];
    }
    return(
        <div>
            <h1>Counter</h1>
            <p>{count}</p>
            <button onClick={handleCount}>Increment</button>
        </div>
    )
}

export default counter;