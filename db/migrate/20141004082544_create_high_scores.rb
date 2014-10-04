class CreateHighScores < ActiveRecord::Migration
  def change
    create_table :high_scores do |t|
      t.belongs_to :user
      t.integer :score
      t.string :game

      t.timestamps
    end
  end
end
