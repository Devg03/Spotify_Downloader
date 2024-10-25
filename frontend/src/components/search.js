import {useState} from "react";

const SearchBar = () => {
    const [inputValue, setInputValue] = useState('');
    
    const handleInputChange = (event) => {
        setInputValue(event.target.value); // Update state with the input value
    };

    const handleSubmit = () => {
        console.log("The input value is:", inputValue); // Do something with the input value
    };
    
    return(
        <div className="search-container">
            <input type="text" placeholder="Search.." name="search" onChange={handleInputChange} />
            <button onClick= {handleSubmit} type="submit">Submit</button>
        </div> 
    );
}

export default SearchBar