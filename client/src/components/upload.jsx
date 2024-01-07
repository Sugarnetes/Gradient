import React, { useMemo, useCallback } from 'react';
import { useDropzone } from 'react-dropzone';

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
    const onDrop = useCallback(async (acceptedFiles) => {
        const pdfFiles = acceptedFiles.filter(file => file.type === 'application/pdf');
    
        if (pdfFiles.length > 0) {
          const formData = new FormData();
          formData.append('pdfFile', pdfFiles[0]); // Assuming you only handle one PDF file
    
          try {
            const response = await fetch('/uploadpdf', {
              method: 'POST',
              body: formData,
            });
    
            if (response.ok) {
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
        <section className="container">
        <div {...getRootProps({style})}>
            <input {...getInputProps()} />
            <p>Drag 'n' drop some files here, or click to select files!</p>
        </div>
        </section>
    );
}

export default Upload;