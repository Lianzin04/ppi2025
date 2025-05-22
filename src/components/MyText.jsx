import styles from './MyText.module.css';

export function MyText() {
  return (
    <div className={styles.container}>
      <div className={styles.div}>
        <h1 className={styles.title}> Meu primeiro ract app </h1>
        <p className={styles.text}> Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquam quas, illo, sit veritatis recusandae libero unde quo laborum dolor nam adipisci?
          Fuga labore temporibus sint quaerat quae ea recusandae nesciunt.
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime nemo consequuntur, tempora quibusdam accusamus exercitationem est laborum asperiores quasi saepe vero expedita sunt, voluptatum enim, accusantium voluptatibus eos officia libero.
        </p>
      </div>
    </div>
  )
}