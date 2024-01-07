import React, { useState, useEffect } from 'react';
import './timer.css';

const Timer = () => {
    const [seconds, setSeconds] = useState(0);
    const [isTimerActive, setIsActive] = useState(false);
    const [timeSelected, setTimeSelected] = useState(0);
    const [websocket, setWebsocket] = useState(null);

    const name = (window.location.href).split('#')[1];

    const toggle = () => {
        if (seconds === 0) {
            window.alert("Please select a time before starting the timer.");
            return;
        }
        setIsActive(!isTimerActive);
    }

    const reset = () => {
        if (!isTimerActive || window.confirm("Are you sure you want to stop the timer?")) { //timer is not active or user confirms
            setIsActive(false);
            setSeconds(0);
            setTimeSelected(0);
        }
    }

    const setTime = (minutes) => {
        if (isTimerActive) {
            window.alert("Please End the timer before changing the time.");
            return;
        }
        setSeconds(minutes * 60);
        setTimeSelected(minutes);
    }

    const complete = () => {
        setSeconds(0);
        setIsActive(false);
        if (isTimerActive) {

            // Create data object to send to Python backend
            const data = name +','+ timeSelected;

            // Send data to Python backend via WebSocket
            if (websocket && websocket.readyState === WebSocket.OPEN) {
                websocket.send(JSON.stringify(data));}

            window.alert(`Time's up! You have completed a ${timeSelected} minute session. Take a break!`);
    
        }
        
    }

    //-----------------WEBSOCKET-----------------//
    useEffect(() => {
        // Establish WebSocket connection
        const ws = new WebSocket('ws://localhost:8888/websocket'); // Corrected URL
        ws.onopen = () => {
            console.log('WebSocket Connected');
        };
        ws.onmessage = (event) => {
            console.log('Message from server ', event.data);
        };
        ws.onerror = (error) => {
            console.error('WebSocket Error ', error);
        };
        ws.onclose = () => {
            console.log('WebSocket Disconnected');
        };
        setWebsocket(ws);

        return () => {
            ws.close(); // Close WebSocket when component unmounts
        };
    }, []);


    //-----------------TIMER-----------------//
    useEffect(() => {
        let interval = null;
        if (isTimerActive && seconds > 0) {
            interval = setInterval(() => {
                setSeconds(seconds => seconds - 1);
            }, 1000);
        } else if (isTimerActive && seconds === 0) {
            complete();
        }

        return () => clearInterval(interval);
    }, [isTimerActive, seconds]);

    const formatTime = () => {
        const minutes = Math.floor(seconds / 60);
        const remainingSeconds = seconds % 60;
        return `${String(minutes).padStart(2, '0')}:${String(remainingSeconds).padStart(2, '0')}`;
    }

    return (
        <>
            <div className="timer">
                <div className="time">
                    {formatTime()}
                </div>
                <div className="buttons">
                    <button onClick={() => setTime(0.05)}>25 min</button>
                    <button onClick={() => setTime(50)}>50 min</button>
                    <button onClick={toggle}>
                        {isTimerActive ? 'Pause' : 'Start'}
                    </button>
                    <button onClick={reset}>End</button>
                </div>
            </div>
        </>
    );
};

/* Debug code for timer, add under button
            <div>
                <p>Time selected: {timeSelected} minutes</p>
                <p>Timer Active: {isTimerActive ? 'Yes' : 'No'}</p> 
                </div>
*/

export default Timer;
