import styles from "./MyGrid.module.css";


export function MyGrid({ title, children }) {
  return (
    <div className={styles.container}>
      <div className={styles.header1}/>
        <div className={styles.header2}/>
        <div className={styles.aside}/>
        <MyGrid></MyGrid>                                                                                                                                
         </div>
  );
}