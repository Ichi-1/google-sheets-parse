import React, { useState, useEffect }from 'react';
import { DataGrid } from '@mui/x-data-grid';
import { useFetch } from 'hooks/useFetch';
import OrderService from 'api/OrderService';

const columns = [
    { field: '#', headerName: 'ID', width: 70 },
    { field: 'Order number', headerName: 'Order number', width: 130 },
    { field: 'Value,$', headerName: 'Value,$', width: 130 },
    { field: 'Supply Date', headerName: 'Supply Date', width: 130 },
];


export const MyTable = () => {
    const [rows, setRows] = useState([])
    const [fetchOrders, isLoading, errors] = useFetch(async () => {
        const response = await OrderService.getOrders()
        const json = await response.json()
        console.log(json.results)
        setRows([json.results])

    })


    useEffect(() => {
        const interval = setInterval(() => {
          fetchOrders();
        }, 5000);
        return () => clearInterval(interval);
    }, []);

    return (
        <div style={{ height: 400, width: '100%' }}>
            <DataGrid
                getRowId={x => Math.random()}
                rows={rows}
                columns={columns}
                pageSize={5}
                rowsPerPageOptions={[5]}
            />
        </div>
    );
}
