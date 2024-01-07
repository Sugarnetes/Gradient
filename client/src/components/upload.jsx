import React, { useMemo, useCallback, useEffect, useState } from 'react';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';

const baseStyle = {
  flex: 1,
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  padding: '20px',
  borderWidth: 2,
  borderRadius: 2,
  borderColor: '#eeeeee',
  borderStyle: 'dashed',
  backgroundColor: '#fafafa',
  color: '#bdbdbd',
  outline: 'none',
  transition: 'border .24s ease-in-out'
};

const focusedStyle = {
  borderColor: '#2196f3'
};

const acceptStyle = {
  borderColor: '#00e676'
};

const rejectStyle = {
  borderColor: '#ff1744'
};

export const Upload = () => {
  const [fileData, setFileData] = useState(null);
  const [location, setLocation] = useState(null);
  const [isInitialLoad, setIsInitialLoad] = useState(false);

  const onDrop = useCallback(async (acceptedFiles) => {
    const pdfFiles = acceptedFiles.filter(file => file.type === 'application/pdf');

    if (pdfFiles.length > 0) {
      const formData = new FormData();
      formData.append('pdfFile', pdfFiles[0]);

      try {
        const response = await axios.post('http://localhost:8888/upload', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        if (response.status === 200) {
          console.log('File uploaded successfully!');
        } else {
          console.error('Failed to upload file.');
        }
      } catch (error) {
        console.error('Error uploading the file:', error);
      }
    } else {
      console.error('No PDF file selected.');
    }
  }, []);

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8888/websocket');
    let isInitialLoad = true;
  
    ws.onopen = () => {
      console.log('WebSocket connected');
      ws.send('request_summary_file');
    };
  
    ws.onmessage = async (event) => {
      const receivedData = event.data;
  
      if (isInitialLoad) {
        isInitialLoad = false;
      } else {
        const receivedFileData = receivedData;
        const blob = new Blob([receivedFileData], { type: 'application/pdf' });
        const fileURL = URL.createObjectURL(blob);
  
        setLocation({ url: fileURL });
        setFileData(receivedFileData);
        ws.send('delete_file_request');
      }
    };
  
    ws.onclose = () => {
      console.log('WebSocket closed');
    };
  
    const handleBeforeUnload = () => {
      ws.send('delete_file_request');
      ws.close();
    };
  
    window.addEventListener("beforeunload", handleBeforeUnload);
  
    return () => {
      window.removeEventListener("beforeunload", handleBeforeUnload);
      ws.close();
    };
  }, []);

  const {
    getRootProps,
    getInputProps,
    isFocused,
    isDragAccept,
    isDragReject
  } = useDropzone({
    onDrop,
    accept: 'application/pdf',
  });

  const style = useMemo(() => ({
    ...baseStyle,
    ...(isFocused ? focusedStyle : {}),
    ...(isDragAccept ? acceptStyle : {}),
    ...(isDragReject ? rejectStyle : {})
  }), [
    isFocused,
    isDragAccept,
    isDragReject
  ]);

  return (
    <section className="container" style={{ position: 'relative' }}>
      <div {...getRootProps({ style })}>
        <input {...getInputProps()} />
        <p>Drag 'n' drop some files here, or click to select files!</p>
      </div>

      {location && (
        <div
          style={{
            position: 'absolute',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            border: '1px solid black',
            padding: '10px',
            backgroundColor: 'white'
          }}
        >
          <iframe
            title="PDF Viewer"
            src={location.url}
            width="400"
            height="300"
            style={{ border: 'none' }}
          />
        </div>
      )}
    </section>
  );
}

export default Upload;