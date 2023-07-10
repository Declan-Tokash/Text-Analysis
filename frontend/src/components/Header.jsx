import React, {useState} from "react";
import './Header.css'
// import sendDataToBackend from "./APIService";

const styles = {
    header: {
        
    },
    headerbtns: {
        margin: '10px',
        marginTop: '20px'
    },
    selectedbtn: {
        margin: '10px',
        marginTop: '20px',
        color: 'blue'
    },
    inputtxt: {
        width: '80%',
        height: '200px',
        marginTop: '10px',
        marginBottom: '5px'
    },
    outputtxt: {
        width: '80%',
        height: '400px',
        margin: '10px'
    }
}

const Header = () => {
    const [action, setAction] = useState();
    const [text, setText] = useState();
    const [responseData, setResponseData] = useState(null);
    const [selectedAction, setSelectedAction] = useState('');
    const actions = ["Summarize", "Translate", "Sentiment Analysis", "Entity Recognition"];

    const sendDataToBackend = (data) => {
        fetch('/process-data', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(data),
        })
          .then(response => response.json())
          .then(responseData => {
            // Access the processed data from the response and do something with it
            console.log(responseData.result);
            setResponseData(responseData.result);
          })
          .catch(error => {
            // Handle any errors that occurred during the request
            console.error('Error:', error);
          });
      }

    const handleButtonClick = (action) => {
        setAction(action);
        setSelectedAction(action);
      };

    const handleTextareaChange = (event) => {
        setText(event.target.value);
      };

    const handleSubmit = () => {
        sendDataToBackend([ action, text ]);
      };
    
    return(
        <div style={styles.header}>
            {actions.map((action, index) => (
                <button 
                    style={action === selectedAction ? styles.selectedbtn : styles.headerbtns} key={index}
                    onClick={() => handleButtonClick(action)}
                >
                    {action}
                </button>
            ))}
            <div>
                <textarea 
                    type="text"
                    placeholder="Enter text here"
                    style={styles.inputtxt}
                    onChange={handleTextareaChange}
                >
                    {text}
                </textarea>
            </div>
            <button onClick={handleSubmit}>Analyze</button>
            <div>
                <textarea 
                        type="text"
                        style={styles.outputtxt}
                        value={responseData || ''}
                        readOnly
                    >
                </textarea>
            </div>
        </div>
    )
}

export default Header;